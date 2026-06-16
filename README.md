# Comfy Audio Nodes

> [!WARNING]
> **Abandoned repository**
>
> This repository is no longer maintained.
>
> Please use **Comfy Random Toolpack** instead:
> `https://github.com/dnnagy/comfy-random-toolpack`
>
> Audio nodes were moved there under the `CRTP_` namespace:
> - `CRTP_NormalizeAudio`
> - `CRTP_AudioProperties`
> - `CRTP_SplitAudioChannels`
> - `CRTP_MergeAudioChannels`

A small collection of ComfyUI audio utility nodes for normalizing volume,
inspecting audio properties, and splitting/merging channels.

## Nodes

### Normalize Audio

Normalize audio volume by peak or RMS level.

Inputs:

- `audio`: ComfyUI `AUDIO` input
- `method`: `peak` or `rms`
- `target_dB`: Target level in dBFS

Output:

- `audio`: Normalized ComfyUI `AUDIO` output

Peak normalization scales each clip so its highest sample reaches the target
level. RMS normalization scales average loudness toward the target and clamps
the result to avoid clipping.

### Audio Properties

Inspect properties of an `AUDIO` signal. The `audio` input is optional; if it
is not connected (or is `None`), `isNone` is `True` and all numeric outputs
are `-1` instead of crashing.

Inputs:

- `audio` (optional): ComfyUI `AUDIO` input

Outputs:

- `samples` (INT): Number of samples per channel
- `duration` (FLOAT): Duration in seconds (`samples / sample_rate`)
- `sample_rate` (INT): Sample rate in Hz
- `num_channels` (INT): Number of channels
- `isNone` (BOOLEAN): `True` if no audio is connected

### Split Audio Channels

Split a multi-channel `AUDIO` into two mono `AUDIO` outputs.

Inputs:

- `audio`: ComfyUI `AUDIO` input

Outputs:

- `left`: First channel as mono `AUDIO`
- `right`: Second channel as mono `AUDIO`

For mono inputs, `left` and `right` are identical. For inputs with more than
two channels, only the first two are returned.

### Merge Audio Channels

Merge two mono `AUDIO` inputs into a single stereo `AUDIO`. The first channel
of each input is used. Sample rates must match; if the lengths differ, the
shorter input is zero-padded.

Inputs:

- `left`: Mono `AUDIO` for the left channel
- `right`: Mono `AUDIO` for the right channel

Output:

- `audio`: Stereo `AUDIO`

## Installation

Clone this repository into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/dnnagy/comfy-audio-nodes.git
```

Restart ComfyUI, then search the node menu under the `audio` category for
`Normalize Audio`, `Audio Properties`, `Split Audio Channels`, or
`Merge Audio Channels`.

## Registry

After publication, this node can be installed with:

```bash
comfy node install comfy-audio-nodes
```

## License

MIT
