---
name: anime-badge-product-maker
description: "Turn anime collectible-figure photos, GK photos, screenshots, or effect renders into a complete badge-product set: circular badge artwork, a photoreal physical button-badge mockup, and a matching sales image that combines the cleaned source figure with the real badge. Use for requests such as ‘实体手办做成徽章并出商品图’, ‘实体手办+实体徽章’, ‘马口铁胸针谷子’, or ‘完整徽章商品流程’. Do not use for badge artwork-only requests that do not need the physical mockup or sales image."
license: MIT
---

# Anime Badge Product Maker

Turn the user's current figure image into one internally consistent product set. The current upload is the source of truth; character identity and physical-product continuity outrank spectacle.

## Default deliverables

Return all three unless the user explicitly narrows the task:

1. `01-badge-art.png` — square canvas with a circular anime badge illustration.
2. `02-badge-mockup.png` — the approved art printed on a photoreal physical tinplate button badge.
3. `03-badge-sales-image.png` — the cleaned real figure/effect image used as background, plus the exact physical badge and the text `马口铁胸针谷子`.

The cleaned background and transparent badge cutout are working assets. Deliver them separately only when the user requests them or when review requires them.

When the user asks to make or revise images, call the available image-generation or image-editing capability and produce the assets. Do not substitute a prompt-only answer. Inspect each result visually before advancing to the next stage, because later stages must reuse the approved prior-stage image rather than regenerate it from prose.

## Input and routing

- One current figure photo, screenshot, GK photo, or effect render is enough for the full workflow. Use it both as character evidence and as the sales-image background source.
- If the user provides several angles, weight them by evidence: face close-ups for identity and eyes, profiles for hair, full-body views for clothing and proportion, close-ups for hands and accessories, and the cleanest frame for the sales background.
- If the source file is missing, expired, unreadable, or no longer available, ask the user to attach it again. Never reconstruct a replacement background from memory, prior generations, or a different character.
- Treat example marketplace screenshots as layout references only. Do not import their character, badge, copy, shop UI, price, or branding.
- Never reuse a previous turn's character or badge unless the user explicitly identifies it as the current product.
- Ask one necessary question only when competing subjects or contradictory references would materially change identity. Otherwise proceed.

## Analyze the source before generation

Create three internal notes.

### Ownership map

Classify each visible item as:

- the main subject's body;
- the subject's clothing, accessory, weapon, action, or power effect;
- a companion creature or display-base motif;
- another character or unrelated object;
- photographic background or household clutter;
- character-name text or a physical base inscription;
- platform UI, seller copy, price, logo, watermark, studio mark, or other removable overlay.

Only the first two categories may define the subject's anatomy. Companion creatures and base motifs may support the composition but must not become the subject's limbs.

### Identity anchors

Record the visible features that must not drift: hairstyle and silhouette; eye state and expression; facial marks; body type and apparent age; clothing construction and palette; gestures; weapon or power effect; accessories; companion motif; and key pose.

Character or franchise knowledge may resolve ambiguity but may not override the current references.

### Text disposition

Decide what happens to every visible text element before editing.

- Preserve a clearly identified character name and a genuine character-name inscription physically present on the display base.
- Do not add a character name that is not visible unless the user asks.
- Remove phone status bars, app controls, carousel dots, download buttons, platform watermarks, seller handles, shop claims, prices, coupons, shipping copy, version labels, photographer or studio marks, and copyright boilerplate.
- Remove franchise titles, logos, and promotional copy by default unless the user explicitly asks to keep them.
- When text is ambiguous, omit it rather than guessing.

Read [references/source-cleanup.md](references/source-cleanup.md) when the source is a busy screenshot, contains several text types, or requires substantial background reconstruction.

## Stage A — source to circular badge artwork

Use the current figure as design evidence and render a polished anime illustration, not a photograph of plastic.

- Use a 1:1 canvas with a centered circular visual area.
- Prefer a bust or half-body composition. Expand only when the action requires it; do not make the subject tiny merely to preserve a full-body view.
- Keep face, head, key gesture, and identity accessories inside the safe area. Secondary effects may approach the edge naturally.
- Fill the entire circle with a coherent background based on supported colors, effects, architecture, creature motifs, or restrained abstract atmosphere.
- Outside the circle may be transparent or clean white. Do not add a decorative or gold rim by default.
- Preserve identity, body type, eye state, expression, clothing, accessories, pose language, weapon, and effect colors.
- Reject extra or fused limbs, malformed hands, duplicate weapons, detached anatomy, and incorrect clothing connections.
- Do not include source UI, character-name typography, seller text, logos, watermarks, or unrelated people inside the badge art unless the user explicitly requests text.

## Stage B — approved art to physical badge

Mode B is an edit of Stage A, not a redesign.

- If the user supplies a physical blank badge photo, edit that target. Otherwise use [assets/default-blank-badge.png](assets/default-blank-badge.png).
- Replace only the printable face. Preserve the real rolled metal rim, thickness, dome, perspective, edge occlusion, reflections, highlight, grain, exposure, contact shadow, and surface texture.
- Place photographic reflections above the inserted art and match sharpness, noise, and color temperature.
- The face, pose, hands, clothing, background elements, and layout must match `01-badge-art.png`. Surface warp, crop, lighting, and edge occlusion are the only permitted changes.
- Reject a flat circular paste-on appearance or any art spilling across the metal rim.

## Stage C — clean the figure background

Clean the user's original figure/effect image for use as the sales background.

- Preserve the actual figure or render: sculpt, pose, proportions, face, clothing, accessories, weapon, power effect, companion motif, display base, material texture, paint, and lighting.
- Do not convert a physical figure into a 2D illustration or replace it with a generic 3D remake.
- Remove UI, platform traces, shop copy, watermarks, unrelated text, household clutter, tools, cups, ashtrays, cables, and distracting objects.
- Preserve a visible character name or physical base inscription according to the text-disposition rules. Remove version labels such as `七武海版本`.
- Reconstruct removed areas cleanly. A restrained studio or atmosphere background may be coordinated with the badge palette when it materially improves the product image, but must not change the figure itself.
- Use a square 1:1 composition. Place the figure left or center-left and reserve useful upper-right and lower-right negative space for copy and the badge. Keep identity-bearing parts and the display base visible.
- Do not add the badge or sales copy during this stage.

## Stage D — isolate the real badge

Create a transparent working cutout from `02-badge-mockup.png`.

- Remove only its surrounding tabletop or background.
- Preserve the complete physical badge silhouette, metal rim, thickness, dome, printed art, photographic reflection, wear, and edge detail.
- Do not redraw, rotate, crop, recolor, beautify, or simplify the badge.
- Reject opaque squares, halos, jagged edges, missing rims, or a generated flat illustration.

## Stage E — compose the sales image

Combine the approved Stage C background and exact Stage D physical badge.

- Prefer literal layer compositing when an image editor or compositor is available. Treat the badge cutout as locked pixels: scale, position, and apply perspective only when needed; create its contact shadow on a separate layer. Do not send the badge through a generative redraw merely to place it.
- Use a 1:1 canvas. Keep the real figure left or center-left.
- Place exactly one badge in the lower-right foreground, usually about 35–42% of canvas width. Keep its complete rim visible and large enough to inspect.
- Do not cover the figure's face, key gesture, weapon or power effect, signature accessory, companion face, or meaningful base inscription.
- Add a realistic contact shadow and restrained environmental reflection so the badge feels physically present. Preserve its original dome highlight and metal material.
- Add the exact Chinese copy `马口铁胸针谷子`. Spell it as seven characters: `马 口 铁 胸 针 谷 子`. Use readable display typography coordinated with the image palette.
- The only other default text allowed is a character name or physical base inscription preserved from the source. Do not add price, coupon, shipping, shop, franchise, studio, seller, English, or Japanese copy unless requested.
- Make the physical badge the primary sale item, the matching figure the supporting context, and the product descriptor secondary.
- Compare the inserted badge against `02-badge-mockup.png`. If its internal art, rim, reflection, or proportions were redrawn, or if a second badge was generated from prose instead of using the cutout, the composition fails.

## Review and correction limit

Read and apply [references/quality-checklist.md](references/quality-checklist.md) before delivery.

- Identity, anatomy, art-to-mockup consistency, physical-badge fidelity, source cleanup, and exact sales copy are hard gates.
- Repair one observable defect at a time and preserve already-correct regions.
- Perform no more than two targeted correction rounds per stage.
- If a hard-gate defect remains after the limit, return the best candidate, state the remaining defect accurately, and wait for direction. Never claim that a failed result passed.

## Delivery boundary

These outputs are high-resolution visual designs and product previews. Do not describe them as print-ready without vendor diameter, bleed, safe-area, resolution, and color-profile requirements.
