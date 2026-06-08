import torch


class NormalizeAudio:
    """Normalize audio volume using peak or RMS normalization."""

    CATEGORY = "audio"
    FUNCTION = "normalize"

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "method": (("peak", "rms"), {"default": "peak"}),
                "target_dB": (
                    "FLOAT",
                    {
                        "default": -1.0,
                        "min": -60.0,
                        "max": 0.0,
                        "step": 0.1,
                        "tooltip": (
                            "Target level in dBFS. "
                            "0.0 = maximum digital level, "
                            "-1.0 = slight headroom (recommended for peak), "
                            "-14.0 = typical broadcast loudness (recommended for RMS)."
                        ),
                    },
                ),
            },
        }

    def normalize(self, audio, method="peak", target_dB=-1.0):
        waveform = audio["waveform"]          # [batch, channels, samples]
        sample_rate = audio["sample_rate"]

        target_linear = 10.0 ** (target_dB / 20.0)

        if method == "peak":
            waveform = self._peak_normalize(waveform, target_linear)
        else:
            waveform = self._rms_normalize(waveform, target_linear)

        return ({"waveform": waveform, "sample_rate": sample_rate},)

    @staticmethod
    def _peak_normalize(waveform: torch.Tensor, target: float) -> torch.Tensor:
        # Normalize per batch item so each clip is treated independently
        peak = waveform.abs().amax(dim=(-2, -1), keepdim=True).clamp(min=1e-8)
        return waveform * (target / peak)

    @staticmethod
    def _rms_normalize(waveform: torch.Tensor, target: float) -> torch.Tensor:
        rms = waveform.pow(2).mean(dim=(-2, -1), keepdim=True).sqrt().clamp(min=1e-8)
        scaled = waveform * (target / rms)
        # Clamp to prevent clipping after RMS scaling
        peak = scaled.abs().amax(dim=(-2, -1), keepdim=True)
        if (peak > 1.0).any():
            scaled = scaled / peak.clamp(min=1e-8)
        return scaled


NODE_CLASS_MAPPINGS = {
    "NormalizeAudio": NormalizeAudio,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NormalizeAudio": "Normalize Audio",
}
