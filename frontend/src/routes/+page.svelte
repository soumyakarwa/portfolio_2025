<script lang="ts">
	import ProjectCard from '../components/ProjectCard/index.svelte';
	import Projects from '$lib/assets/projects/content.json';

	const COL_SPAN = 8;
	const ROW_SPAN = 6;

	let active = $state(-1);
	let activeProject = $state('');
</script>

<div class="grid h-full w-full grid-cols-24 grid-rows-14">
	{#each Projects as project, i}
		<div
			role="button"
			tabindex={0}
			class={[
				'relative opacity-0 transition-opacity duration-100 ease-linear hover:cursor-pointer hover:opacity-100',
				active === i ? 'z-50' : 'z-10',
				active !== -1 && active !== i ? 'pointer-events-none' : ''
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
				overview={project.overview}
				supporting={project.supporting}
				activeIndex={activeProject}
			/>
		</div>
	{/each}
</div>
