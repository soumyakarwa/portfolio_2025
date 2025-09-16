<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { goto } from '$app/navigation';

	interface Props {
		id: string;
		title: string;
		overview: string;
		activeIndex: string;
	}

	let { id, title, overview, activeIndex }: Props = $props();

	const offset = 0;
	const jitter = 90;
	const count = 6;
	const delay = 60; // ms between items
	const duration = 300; // ms per item
	const step = 360 / count;

	let imageWidth = $state(0);
	let imageHeight = $derived((imageWidth * 9) / 16);

	const R = $derived(Math.max(imageWidth, imageHeight) / 2 + offset);

	let isActive = $derived(activeIndex === id);

	const rFor = (i: number) => R + (jitter ? (Math.random() * 2 - 1) * jitter : 0);
	const open = () => goto(`/project/${id}`);
</script>

<div class="pointer-events-none absolute inset-0 z-0">
	{#each Array.from({ length: count }) as _, i}
		{#if isActive}
			<div
				in:fade={{ delay: i * delay, duration }}
				class="absolute top-1/2 left-1/2 z-0 border-[0.5px] border-solid border-black"
				style={`width:${imageWidth * 0.75}px; height:${imageHeight * 0.75}px;
                transform: translate(-50%,-50%)
                           rotate(${i * step}deg)
                           translate(${rFor(i)}px)
                           rotate(${-i * step}deg);`}
			></div>
		{/if}
	{/each}
</div>

<div
	id={`project-${id}`}
	class="absolute z-10 flex h-full w-full flex-col justify-around gap-3 bg-white p-3"
	style:background-image="var(--dashed-border)"
	role="link"
	tabindex="0"
	onclick={() => open()}
	onkeydown={(e) => e.key === 'Enter' && open()}
>
	<div class="w-full bg-black" bind:clientWidth={imageWidth} style:height="{imageHeight}px"></div>
	<div class="flex flex-col">
		<div class="text-base font-bold uppercase">{title}</div>
		<div class="text-xs">{overview}</div>
	</div>
</div>
