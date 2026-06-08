# Comfy Audio Nodes

A small collection of ComfyUI audio nodes. It currently includes one node for normalizing audio volume by peak or RMS level.

## Node

### Normalize Audio

Inputs:

- `audio`: ComfyUI `AUDIO` input
- `method`: `peak` or `rms`
- `target_dB`: Target level in dBFS

Output:

- `audio`: Normalized ComfyUI `AUDIO` output

Peak normalization scales each clip so its highest sample reaches the target level. RMS normalization scales average loudness toward the target and clamps the result to avoid clipping.

## Installation

Clone this repository into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/dnnagy/comfy-audio-nodes.git
```

Restart ComfyUI, then search for `Normalize Audio` in the node menu.

## Registry

After publication, this node can be installed with:

```bash
comfy node install comfy-audio-nodes
```

## License

MIT
