<script lang="ts">
	import Navbar from '../components/Navbar/index.svelte';
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();

	const links = [
		{
			label: 'WORK',
			href: '/'
		},
		{
			label: 'ABOUT',
			href: '/about'
		}
	];

	const socialLinks = [
		{
			label: 'EMAIL',
			href: 'mailto:soumyakarwa01@gmail.com'
		},
		{
			label: 'INSTAGRAM',
			href: 'https://www.instagram.com/sk.arwaa/'
		},
		{
			label: 'GITHUB',
			href: 'https://github.com/soumyakarwa'
		},
		{
			label: 'LINKEDIN',
			href: 'https://www.linkedin.com/in/soumyakarwa/'
		}
	];

	const name = ['SOUMYA', 'KARWA'];
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="relative flex h-screen w-screen flex-row gap-2 p-6">
	<div class="absolute top-[0.75rem] right-[2.3rem] flex flex-row gap-[8px]">
		{#each name as word}
			<div class="flex flex-row">
				{#each word.split('') as letter}
					<span class="bg-white">{letter}</span>
				{/each}
			</div>
		{/each}
	</div>
	<div class="w-max-content items-between flex h-full flex-col justify-between">
		<Navbar {links} textClass={'text-uppercase text-base'} />
		<Navbar links={socialLinks} textClass={'text-xs'} />
	</div>

	<div class="h-full w-screen p-6" style="background-image:var(--dashed-border)">
		{@render children?.()}
	</div>
</div>
