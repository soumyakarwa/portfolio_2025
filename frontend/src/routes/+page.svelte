<script lang="ts">
	import ProjectCard from '$lib/components/ProjectCard/index.svelte';
	import Projects from '$lib/assets/content/content.json';
	import { isDesktop, isGridLayout } from '$lib/components/Util/index';
	import { fade } from 'svelte/transition';

	const COL_SPAN = 8;
	const ROW_SPAN = 6;

	let active = $state(-1);
	let activeProject = $state('');
</script>

{#if $isGridLayout}
	<div
		class="grid auto-rows-max grid-cols-1 gap-4 hover:cursor-pointer md:grid-cols-2 lg:grid-cols-3"
		transition:fade
	>
		{#each Projects as project, i}
			<ProjectCard
				id={project.id}
				title={project.title}
				tag={project.tag}
				supporting={project.supporting}
				activeIndex={activeProject}
			/>
		{/each}
	</div>
{:else}
	<div class="grid h-full w-full" transition:fade>
		{#each Projects as project, i}
			<div
				role="button"
				tabindex={0}
				class={[
					'h-auto w-full opacity-0 transition-opacity duration-200 ease-linear hover:cursor-pointer hover:opacity-100 lg:relative',
					$isDesktop && active === i ? 'z-50' : 'z-10',
					$isDesktop && active !== -1 && active !== i ? 'pointer-events-none' : ''
				]}
				style:grid-column-start={project.position[0]}
				style:grid-column-end={project.position[0] + COL_SPAN}
				style:grid-row-start={project.position[1]}
				style:grid-row-end={project.position[1] + ROW_SPAN}
				onmouseenter={() => {
					active = i;
					activeProject = project.id;
				}}
				onmouseleave={() => {
					active = -1;
					activeProject = '';
				}}
			>
				<ProjectCard
					id={project.id}
					title={project.title}
					tag={project.tag}
					supporting={project.supporting}
					activeIndex={activeProject}
				/>
			</div>
		{/each}
	</div>
{/if}
