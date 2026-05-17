---
name: seedance
description: "Generate videos with ByteDance Seedance 2.0 via inference.sh CLI. Unified model for text-to-video, image-to-video, and reference-to-video with synchronized audio, up to 1080p, 4-15s duration. Pro and Fast variants. Use for: social media videos, music videos, product demos, animated content, AI video with sound. Triggers: seedance, seedance 2, bytedance video, seedance t2v, seedance i2v, seedance r2v, video with audio, seedance 2.0, bytedance seedance"
allowed-tools: Bash(belt *)
---

> **Install the belt CLI skill:** `npx skills add belt-sh/cli`

# Seedance 2.0 Video Generation

Generate videos with synchronized audio using ByteDance's Seedance 2.0 via [inference.sh](https://inference.sh) CLI.

## Quick Start

> Requires inference.sh CLI (`belt`). [Install instructions](https://raw.githubusercontent.com/inference-sh/skills/refs/heads/main/cli-install.md)

```bash
belt login

belt app run bytedance/seedance-2-0 --input '{
  "prompt": "a jazz band performing in a dimly lit club",
  "generate_audio": true
}'
```


## Models

| Model | App ID | Best For |
|-------|--------|----------|
| Seedance 2.0 | `bytedance/seedance-2-0` | Best quality, up to 1080p, text/image/reference-to-video |
| Seedance 2.0 Fast | `bytedance/seedance-2-0-fast` | Faster generation, same capabilities |

Both models support text-to-video, image-to-video, reference-to-video, up to 1080p resolution, 4-15s duration, and synchronized audio generation.

## Examples

### Text-to-Video with Audio

```bash
belt app run bytedance/seedance-2-0 --input '{
  "prompt": "ocean waves crashing on rocks during a storm, dramatic cinematic shot",
  "generate_audio": true,
  "duration": 10,
  "ratio": "16:9"
}'
```

### Fast Mode (Cheaper)

```bash
belt app run bytedance/seedance-2-0-fast --input '{
  "prompt": "a butterfly landing on a flower in slow motion",
  "generate_audio": true
}'
```

### Image-to-Video

Animate a still image into a video:

```bash
belt app run bytedance/seedance-2-0 --input '{
  "image": "https://your-image.jpg",
  "prompt": "gentle camera movement, leaves rustling in the wind",
  "generate_audio": true
}'
```

### Image-to-Video with Start and End Frames

```bash
belt app run bytedance/seedance-2-0 --input '{
  "image": "https://start-frame.jpg",
  "end_image": "https://end-frame.jpg",
  "prompt": "smooth transition between scenes",
  "generate_audio": true
}'
```

### Reference-to-Video

Use reference images, videos, or audio to guide generation:

```bash
belt app run bytedance/seedance-2-0 --input '{
  "prompt": "A person who looks like the reference walking through a garden",
  "reference_image": "https://portrait.jpg",
  "generate_audio": true
}'
```

### Multi-Reference

```bash
belt app run bytedance/seedance-2-0 --input '{
  "prompt": "Two people having a conversation at a cafe",
  "reference_image": "https://person1.jpg",
  "reference_image_2": "https://person2.jpg",
  "generate_audio": true
}'
```

### Reference with Audio

```bash
belt app run bytedance/seedance-2-0 --input '{
  "prompt": "A musician performing a song",
  "reference_image": "https://musician.jpg",
  "reference_audio": "https://music.mp3",
  "generate_audio": true
}'
```

### Reference with Video

```bash
belt app run bytedance/seedance-2-0 --input '{
  "prompt": "Recreate this scene in a different setting",
  "reference_video": "https://reference-clip.mp4",
  "generate_audio": true
}'
```

## Pricing

| Model | Pricing |
|-------|---------|
| Seedance 2.0 | $4.30-$7.70/M tokens (varies by resolution and input type) |
| Seedance 2.0 Fast | $3.30-$5.60/1K tokens |

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | string | required | Text description of the video |
| `generate_audio` | boolean | false | Generate synchronized audio |
| `duration` | integer | - | Duration in seconds (4-15), or -1 for auto |
| `ratio` | enum | - | 16:9, 9:16, 1:1, 4:3, 3:4, or adaptive |
| `resolution` | enum | - | Up to 1080p |
| `seed` | integer | random | Reproducible generation |
| `watermark` | boolean | - | Add watermark to output |
| `image` | file | - | First-frame image for image-to-video |
| `end_image` | file | - | Last-frame image for first+last frame control |
| `reference_image` | file | - | Reference image for reference-to-video |
| `reference_image_2` | file | - | Second reference image |
| `reference_image_3` | file | - | Third reference image |
| `reference_video` | file | - | Reference video |
| `reference_audio` | file | - | Reference audio |

## Search Seedance Apps

```bash
belt app list --search "seedance"
```

## Related Skills

```bash
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# All video generation models
npx skills add inference-sh/skills@ai-video-generation

# Google Veo
npx skills add inference-sh/skills@google-veo

# Image generation (for image-to-video)
npx skills add inference-sh/skills@ai-image-generation

# AI avatars & lipsync
npx skills add inference-sh/skills@ai-avatar-video
```

Browse all video apps: `belt app list --category video`

## Documentation

- [Running Apps](https://inference.sh/docs/apps/running) - How to run apps via CLI
- [Streaming Results](https://inference.sh/docs/api/sdk/streaming) - Real-time progress updates
- [Content Pipeline Example](https://inference.sh/docs/examples/content-pipeline) - Building media workflows
