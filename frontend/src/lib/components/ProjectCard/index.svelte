<script lang="ts">
	import { fade } from 'svelte/transition';
	import { goto } from '$app/navigation';
	import { isDesktop } from '$lib/components/Util/index';

	interface Props {
		id: string;
		title: string;
		overview: string;
		supporting: string[];
		activeIndex: string;
	}

	let { id, title, overview, supporting, activeIndex }: Props = $props();

	const imgSrc = `/assets/${id}/hero.gif`;
	const offset = 0;
	const jitter = 100;

	const delay = 60; // ms between items
	const duration = 300; // ms per item

	const step = supporting.length > 0 ? 360 / supporting.length : 1;

	let imageWidth = $state(0);
	let imageHeight = $state(0);
	// let imageHeight = $derived((imageWidth * 9) / 16);
	let containerWidth = $state(0);
	let containerHeight = $state(0);

	const R = $derived(Math.max(containerWidth, containerHeight) * 0.5 + offset);

	let isActive = $derived(activeIndex === id);

	const rFor = (i: number) => R; //+ (jitter ? (Math.random() * 2 - 1) * jitter : 0)
	const open = () => goto(`/project/${id}`);

	let imgDim: { width: number; height: number }[] = $derived(
		supporting.map(() => ({
			width: imageWidth * 0.55,
			height: 0
		}))
	);
</script>

{#if supporting.length > 0 && $isDesktop}
	<div class="pointer-events-none absolute inset-0 z-0">
		{#each supporting as src, i}
			{#if isActive}
				<img
					in:fade={{ delay: (i + 1) * delay, duration }}
					src={`/assets/${id}/${src}`}
					class="absolute top-1/2 left-1/2 z-0 h-auto"
					alt="gif showcasing project demo"
					style:width="{imageWidth * 0.55}px"
					style:transform={`translate(-50%,-50%) rotate(${i * step}deg) translate(${rFor(i)}px) rotate(${-i * step}deg)`}
				/>
			{/if}
		{/each}
	</div>
{/if}
<div
	id={`project-${id}`}
	class="z-10 flex h-full w-full flex-col justify-around gap-1 bg-white p-3 lg:absolute"
	style:background-image="var(--dashed-border)"
	role="link"
	tabindex="0"
	onclick={() => open()}
	onkeydown={(e) => e.key === 'Enter' && open()}
	bind:clientHeight={containerHeight}
	bind:clientWidth={containerWidth}
	style:min-height="{imageHeight}px"
>
	<img
		src={imgSrc}
		class="h-auto w-full"
		alt="gif showcasing project demo"
		bind:clientWidth={imageWidth}
		bind:clientHeight={imageHeight}
	/>
	<!-- <div class="flex flex-col"> -->
	<div class="text-base font-bold uppercase">{title}</div>
	<!-- <div class="text-xs">{overview}</div> -->
	<!-- </div> -->
</div>
