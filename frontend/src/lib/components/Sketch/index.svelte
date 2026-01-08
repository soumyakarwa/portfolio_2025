<script lang="ts">
	import P5 from 'p5-svelte';
	import type p5 from 'p5';

	interface Props {
		width: number;
		height: number;
	}

	let { width, height }: Props = $props();

	const sketch = (p: p5) => {
		let progress = 0;
		const speed = 0.05;

		// Different extents → not 45°
		const halfWidth = width / 225;
		const halfHeight = halfWidth * 1.1;
		const triggerRadius: number = width / 12.5;

		let cx: number;
		let cy: number;

		const randomizePosition = () => {
			cx = p.random(0.1, 0.9) * p.width;
			cy = p.random(0.1, 0.9) * p.height;
			progress = 0;
		};

		p.setup = () => {
			p.createCanvas(width, height);
			p.stroke('#8F2D56');
			p.strokeWeight(2.5);
			p.noFill();

			randomizePosition();
		};

		p.draw = () => {
			p.clear();

			const d = p.dist(p.mouseX, p.mouseY, cx, cy);
			const mouseNear = d < triggerRadius;

			// Relocate when mouse reaches the cross
			if (mouseNear) {
				randomizePosition();
			}
			progress = p.min(progress + speed, 2);

			// --- Pulsing scale when idle ---
			let pulse = 2;
			if (!mouseNear) {
				pulse = 1 - 0.15 * p.sin(p.frameCount * 0.05);
			}

			p.push();
			p.translate(cx, cy);
			p.scale(pulse);
			p.translate(-cx, -cy);

			// --- Phase 1: "\" left → right ---
			if (progress > 0) {
				const t1 = p.min(progress, 1);
				const x = p.lerp(cx - halfWidth, cx + halfWidth, t1);
				const y = p.lerp(cy - halfHeight, cy + halfHeight, t1);
				p.line(cx - halfWidth, cy - halfHeight, x, y);
			}

			// --- Phase 2: "/" left → right ---
			if (progress > 1) {
				const t2 = p.min(progress - 1, 1);
				const x = p.lerp(cx - halfWidth, cx + halfWidth, t2);
				const y = p.lerp(cy + halfHeight, cy - halfHeight, t2);
				p.line(cx - halfWidth, cy + halfHeight, x, y);
			}

			p.pop();
		};
	};
</script>

<P5 {sketch} />
