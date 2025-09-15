<script lang="ts">
	import ProjectCard from '../components/ProjectCard/index.svelte';

	const content = {
		id: '1',
		title: 'The Most Iconic Duo In Brooklyn Nine-Nine',
		overview:
			'Designed and developed a visual essay titled “The Most Iconic Duo in Brooklyn Nine-Nine” to identify the most beloved character duo in the sitcom Brooklyn Nine-Nine by analyzing official and unofficial episode descriptions, IMDb ratings, and votes. Honorable mention in the 2024 Pudding Cup, Longlisted in the 2024 Information is Beautiful Awards.'
	};
</script>

<div class="relative h-full w-full">
	<!-- {#each content as card} -->
	<ProjectCard id={content.id} title={content.title} overview={content.overview} />
	<!-- {/each} -->
</div>
