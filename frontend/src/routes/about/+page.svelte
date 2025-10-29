<script lang="ts">
	import data from '$lib/assets/content/about.json';
</script>

<div class="relative flex flex-col gap-6">
	<div class="max-w-content fixed flex flex-col bg-white p-1 text-base font-bold uppercase">
		{@html data[0].title}
	</div>
	<!-- opacity-0 title for positioning -->
	<div class="flex flex-col gap-1 p-1 text-base font-bold uppercase opacity-0">
		{@html data[0].title}
	</div>

	<div class="flex flex-col gap-3 lg:gap-9">
		{#each data[0].paragraphs as para, i}
			<div id={para.title} class="flex scroll-mt-24 flex-col gap-3 lg:flex-row lg:gap-9">
				<div class="flex w-full flex-col gap-[2px] lg:w-1/3">
					<div class="text-xs font-extrabold uppercase">{@html para.title}</div>
					<div class="text-xs">{@html para.content}</div>
				</div>
				{#if para.images.length > 0}
					<div class="flex h-auto w-full flex-col gap-3 lg:w-1/2">
						{#each para.images as images, j}
							<img
								class="h-auto w-full"
								src={`/assets/me/${images.src}`}
								alt={`supporting image about ${images.src} `}
							/>
						{/each}
					</div>
				{/if}
			</div>
		{/each}
	</div>
</div>
