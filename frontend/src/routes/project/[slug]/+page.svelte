<script lang="ts">
	import { fade } from 'svelte/transition';
	import type { PageProps } from './$types';
	import { activeId, scrollY } from '$lib/components/Util/index';
	import { onMount, tick } from 'svelte';

	let { data }: PageProps = $props();

	let container: HTMLElement | null | undefined = $state();
	let paras: { node: HTMLElement | null; bounds: number[] }[] = $state(
		Array.from({ length: data.paragraphs?.length || 0 }, () => ({
			node: null,
			bounds: [0, 0]
		}))
	);

	onMount(async () => {
		await tick();

		paras.forEach((p, i) => {
			if (!p?.node) return;

			const currY = p.node.getBoundingClientRect().bottom;

			if (i === 0) {
				p.bounds = [0, currY];
			} else {
				const prev = paras[i - 1];
				const prevTop = prev?.node?.getBoundingClientRect().top;
				if (typeof prevTop === 'number') {
					p.bounds = [prevTop, currY];
				}
			}
		});
	});

	$effect(() => {
		paras.forEach((p) => {
			if (p.node && $scrollY > p.bounds[0] && $scrollY < p.bounds[1]) {
				activeId.set(p.node.id);
			}
		});
	});
</script>

<div class="flex flex-col gap-6" transition:fade bind:this={container}>
	<!-- <div class="flex flex-row justify-between"> -->
	<div class="text-base font-extrabold uppercase">{data.title}</div>
	<!-- <div class="text-base font-bold uppercase">0%</div>
	</div> -->
	{#if data.paragraphs}
		<div class="flex flex-col gap-3 lg:gap-9">
			{#each data.paragraphs as para, i}
				<div
					id={para.href
						? para.href.toLowerCase().replace(/\s+/g, '-')
						: para.title.toLowerCase().replace(/\s+/g, '-')}
					class="flex scroll-mt-6 flex-col gap-3 lg:flex-row lg:gap-9"
					bind:this={paras[i].node}
				>
					<div class="flex w-full flex-col gap-[2px] lg:w-1/3">
						<div class="text-xs font-extrabold uppercase">{@html para.title}</div>
						<div class="text-xs">{@html para.content}</div>
					</div>
					<div class="flex h-auto w-full flex-col gap-3 lg:w-1/2">
						{#each para.images as images, j}
							<img
								class="h-auto w-full"
								src={`/assets/${data.id}/${images.src}`}
								alt={`supporting image about ${images.src} `}
							/>
						{/each}
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
