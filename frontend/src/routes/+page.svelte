<script lang="ts">
	import ProjectCard from '$lib/components/ProjectCard/index.svelte';
	import Projects from '$lib/assets/projects/content.json';
	import { isDesktop, isGridLayout } from '$lib/components/Util/index';

	const COL_SPAN = 8;
	const ROW_SPAN = 6;

	let active = $state(-1);
	let activeProject = $state('');
</script>

<div
	class={[
		'grid-rows-auto grid w-full grid-cols-1 gap-4 md:grid-cols-2',
		$isDesktop ? 'h-full' : '',
		$isGridLayout ? 'lg:grid-cols-3' : 'lg:grid-cols-24 lg:grid-rows-14 lg:gap-0'
	]}
>
	{#each Projects as project, i}
		<div
			role="button"
			tabindex={0}
			class={[
				'opacity-100 transition-opacity duration-200 ease-linear hover:cursor-pointer hover:opacity-100 lg:relative',
				$isDesktop && active === i ? 'z-50' : 'z-10',
				$isDesktop && active !== -1 && active !== i ? 'pointer-events-none' : '',
				$isGridLayout ? ' lg:opacity-100' : 'lg:opacity-0'
			]}
			style:grid-column-start={!$isGridLayout ? project.position[0] : null}
			style:grid-column-end={!$isGridLayout ? project.position[0] + COL_SPAN : null}
			style:grid-row-start={!$isGridLayout ? project.position[1] : null}
			style:grid-row-end={!$isGridLayout ? project.position[1] + ROW_SPAN : null}
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
				overview={project.overview}
				supporting={project.supporting}
				activeIndex={activeProject}
			/>
		</div>
	{/each}
</div>
