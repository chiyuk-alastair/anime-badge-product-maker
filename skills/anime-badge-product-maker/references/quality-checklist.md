# Quality Checklist

Review every generated or edited image. A failed hard gate requires a targeted correction before delivery.

## A. Circular badge artwork

### Identity and anatomy — hard gates

- [ ] Same subject as the current source, not a generic canonical replacement or a previous task's character.
- [ ] Hair, face, eye state, expression, body type, clothing, accessory, weapon or power effect, and key pose are supported by the source.
- [ ] No foreign limbs, extra hands, duplicated weapons, fused anatomy, detached parts, or implausible finger connections.
- [ ] Companion creatures and display effects remain visually distinct from the subject's anatomy.

### Composition and finish

- [ ] 1:1 canvas with a clear centered circular design and complete background coverage.
- [ ] Subject remains dominant; face, head, key gesture, and identity accessories stay within the safe area.
- [ ] No unintended text, UI, logo, watermark, seller mark, studio mark, or decorative gold rim.
- [ ] Polished anime illustration rather than figure photography, waxy rendering, or low-quality AI output.

## B. Physical badge mockup

### Artwork consistency — hard gates

- [ ] Uses the approved `01-badge-art.png` rather than a redraw.
- [ ] Face, gesture, clothing, background elements, and relative layout match the approved art.
- [ ] Only perspective, surface crop, brightness, reflection, curvature, and edge occlusion changed.

### Physical realism — hard gates

- [ ] Metal rim, thickness, dome, silhouette, reflection, grain, and contact shadow remain convincing.
- [ ] Artwork follows the surface and stays inside the printable face.
- [ ] Result does not look like a flat circle pasted onto a photograph.

## C. Clean figure background

### Source fidelity — hard gates

- [ ] Preserves the actual figure or render, pose, proportions, face, clothing, accessories, effect parts, companion motif, display base, and material style.
- [ ] Physical figures remain photographic; they are not replaced by illustrations or generic remakes.
- [ ] Character-name text and genuine base inscriptions are preserved when visible.
- [ ] Version labels, platform UI, seller text, watermarks, studio marks, prices, and unrelated copy are removed.
- [ ] Household or workshop clutter is removed without deleting genuine product parts.
- [ ] No obvious inpainting seams or unexplained floating objects.

### Composition

- [ ] Square layout leaves usable upper-right and lower-right space.
- [ ] Face, signature effect, key accessory, shoes, and display base are not incorrectly cropped.

## D. Badge cutout

- [ ] Complete physical badge silhouette and rim are present.
- [ ] Printed art, dome reflection, proportions, edge texture, and color match `02-badge-mockup.png`.
- [ ] Background is transparent with no opaque square, fabric residue, halo, or jagged edge.

## E. Final sales image

### Product fidelity — hard gates

- [ ] Exactly one real physical badge is present.
- [ ] Badge art, metal rim, highlight, curvature, and proportions match `02-badge-mockup.png`; it was not redrawn as a flat illustration.
- [ ] The badge is the Stage D cutout placed as a locked layer whenever literal compositing is available; generative editing did not silently replace it.
- [ ] Badge has believable scale, perspective, contact shadow, and environmental reflection.
- [ ] Figure and badge clearly depict the same subject and visual theme.

### Layout and text — hard gates

- [ ] The badge does not cover the figure's face, key gesture, signature accessory, companion face, or meaningful base inscription.
- [ ] Exact copy reads `马口铁胸针谷子` with all seven characters correct.
- [ ] No platform UI, price, coupon, shipping claim, seller watermark, studio branding, or unrequested promotional copy.
- [ ] Any preserved character name is accurate and came from the source.

## F. Delivery

- [ ] Full workflow contains `01-badge-art.png`, `02-badge-mockup.png`, and `03-badge-sales-image.png` unless the user narrowed scope.
- [ ] All three outputs refer to the current source and remain mutually consistent.
- [ ] Visual previews are not described as production-ready without vendor print specifications.

## Correction strategy

1. Repair identity, anatomy, exact badge fidelity, source cleanup, and exact text before decorative issues.
2. Describe one observable defect per correction.
3. Preserve already-correct features and layout.
4. Stop after two automatic correction rounds per stage and disclose any remaining hard-gate defect.
