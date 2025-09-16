<script lang="ts">
	import ProjectCard from '../components/ProjectCard/index.svelte';

	// const content = {
	// 	id: '1',
	// 	title: 'The Most Iconic Duo In Brooklyn Nine-Nine',
	// 	overview:
	// 		'Designed and developed a visual essay titled “The Most Iconic Duo in Brooklyn Nine-Nine” to identify the most beloved character duo in the sitcom Brooklyn Nine-Nine by analyzing official and unofficial episode descriptions, IMDb ratings, and votes. Honorable mention in the 2024 Pudding Cup, Longlisted in the 2024 Information is Beautiful Awards.'
	// };

	const positions = [
		[1, 4],
		[4, 7],
		[16, 1],
		[10, 3],
		[13, 6],
		[3, 1]
	];

	const projects = positions.map(([c, r], i) => {
		return {
			id: String(i + 1),
			title: `Project ${i + 1}`,
			overview: `Overview for project ${i + 1}`
		};
	});

	const COL_SPAN = 8,
		ROW_SPAN = 5;

	let active = $state(-1);
</script>

<div class="grid h-full w-full grid-cols-24 grid-rows-12 gap-2">
	{#each projects as project, i}
		<div
			role="button"
			tabindex={0}
			class={[
				'relative opacity-0 transition-opacity duration-100 ease-linear hover:cursor-pointer hover:opacity-100',
				active === i ? 'z-50' : 'z-10',
				active !== -1 && active !== i ? 'pointer-events-none' : ''
			]}
			style:grid-column-start={positions[i][0]}
			style:grid-column-end={positions[i][0] + COL_SPAN}
			style:grid-row-start={positions[i][1]}
			style:grid-row-end={positions[i][1] + ROW_SPAN}
			onmouseenter={() => (active = i)}
			onmouseleave={() => (active = -1)}
		>
			<ProjectCard
				id={project.id}
				startingPos={positions[i]}
				title={project.title}
				overview={project.overview}
				isActive={active == i}
			/>
		</div>
	{/each}
</div>
