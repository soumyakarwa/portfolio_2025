<script lang="ts">
	import { fade } from 'svelte/transition';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<div class="flex flex-col gap-6" transition:fade>
	<div class="text-base font-bold uppercase">{data.title}</div>
	{#if data.paragraphs}
		<div class="flex flex-col gap-9">
			{#each data.paragraphs as para, i}
				<div class="flex flex-row gap-9">
					<div class="flex w-1/3 flex-col gap-[2px]">
						<div class="text-xs font-bold uppercase">{@html para.title}</div>
						<div class="text-xs">{@html para.content}</div>
					</div>
					<div class="flex h-auto w-1/2 flex-col gap-3">
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
