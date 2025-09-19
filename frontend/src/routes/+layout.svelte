<script lang="ts">
	import Navbar from '../components/Navbar/index.svelte';
	import { page } from '$app/state';
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { writable } from 'svelte/store';

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

	let containerWidth: number = $state(0);

	let projectLinks = $derived(
		page.data?.paragraphs?.map((p: { title: string; href: string }) => ({
			label: p.href ? p.href : p.title,
			href: p.href ? `#${p.href}` : `#${p.title.toLowerCase().replace(/\s+/g, '-')}`
		})) ?? null
	);
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="relative flex h-screen w-screen flex-row gap-2 p-6">
	<div class="absolute top-[0.75rem] right-[2.3rem] z-10 flex flex-row gap-[8px]">
		{#each name as word}
			<div class="flex flex-row">
				{#each word.split('') as letter}
					<span class="bg-white">{letter}</span>
				{/each}
			</div>
		{/each}
	</div>
	<div class="items-between flex h-full w-1/12 flex-col justify-between">
		<Navbar {links} textClass={'text-uppercase text-base'} />
		{#if projectLinks}
			<Navbar links={projectLinks} textClass={'text-xs'} />
		{/if}
		<Navbar links={socialLinks} textClass={'text-xs'} />
	</div>

	<div
		class="h-full w-full overflow-y-auto scroll-smooth p-6"
		style="background-image:var(--dashed-border)"
		bind:clientWidth={containerWidth}
	>
		{@render children?.()}
	</div>

	<div
		class="absolute right-6 bottom-6 mr-[0.5px] mb-[0.75px] ml-[0.5px] h-1/20 bg-gradient-to-t from-white to-transparent"
		style:width="{containerWidth - 1}px"
	></div>
	<div
		class="absolute top-6 right-6 mt-[0.5px] mr-[0.5px] ml-[0.5px] h-1/50 bg-gradient-to-b from-white to-transparent"
		style:width="{containerWidth - 1}px"
	></div>
</div>
