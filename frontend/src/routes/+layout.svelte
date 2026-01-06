<script lang="ts">
	import Navbar from '$lib/components/Navbar/index.svelte';
	import ToggleSwitch from '$lib/components/ToggleSwitch/index.svelte';
	import { page } from '$app/state';
	import '../app.css';
	import favicon from '$lib/assets/logo.png';
	import { scrollY, isMenuOpen, isDesktop, isGridLayout, awards } from '$lib/components/Util/index';

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
	let containerHeight: number = $state(0);
	let screenWidth: number = $state(0);
	let checked: boolean = $state(true);
	let m: { x: number; y: number } = $state({ x: 0, y: 0 });
	// let isGrid: boolean = $derived(checked && $isDesktop);

	let projectLinks = $derived(
		page.data?.paragraphs?.map((p: { title: string; href: string }) => ({
			label: p.href ? p.href : p.title,
			href: p.href
				? `#${p.href.toLowerCase().replace(/\s+/g, '-')}`
				: `#${p.title.toLowerCase().replace(/\s+/g, '-')}`
		})) ?? null
	);

	const onScroll = (e: Event) => {
		const el = e.currentTarget as HTMLElement;
		scrollY.set(el.scrollTop);
	};

	const handleMousemove = (event: MouseEvent) => {
		m.x = event.clientX;
		m.y = event.clientY;
	};

	$effect(() => {
		isDesktop.set(screenWidth >= 1024);
		isGridLayout.set(!$isDesktop || checked);
		if (isDesktop) {
			isMenuOpen.set(false);
		}
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<svelte:window bind:innerWidth={screenWidth} />

<!-- svelte-ignore a11y_no_static_element_interactions -->
<div class="relative flex h-screen w-screen flex-row gap-2 p-6" onmousemove={handleMousemove}>
	<button
		type="button"
		class="absolute top-6 left-6 z-60 flex translate-x-1/2 -translate-y-1/2 cursor-pointer flex-col gap-[3px] bg-white lg:hidden"
		style="background-image:var(--dashed-border)"
		aria-expanded={$isMenuOpen}
		aria-controls="primary-nav"
		aria-label={$isMenuOpen ? 'Close navigation menu' : 'Open navigation menu'}
		onclick={() => isMenuOpen.set(!$isMenuOpen)}
	>
		<span
			class="material-symbols-outlined pointer-events-none absolute inset-0 grid place-items-center
           transition-all duration-200 ease-out
           [@media(prefers-reduced-motion:reduce)]:transition-none
           {$isMenuOpen ? 'scale-90 rotate-90 opacity-0' : 'scale-100 rotate-0 opacity-100'}"
			aria-hidden="true">menu</span
		>
		<!-- close (X) -->
		<span
			class="material-symbols-outlined pointer-events-none grid place-items-center
           transition-all duration-200 ease-out
           [@media(prefers-reduced-motion:reduce)]:transition-none
           {$isMenuOpen ? 'scale-100 rotate-0 opacity-100' : 'scale-90 -rotate-90 opacity-0'}"
			aria-hidden="true">close</span
		>
	</button>

	<div class="absolute top-[0.75rem] right-[2.3rem] z-50 flex flex-row gap-[8px]">
		{#each name as word}
			<div class="flex flex-row">
				{#each word.split('') as letter}
					<span class="bg-white">{letter}</span>
				{/each}
			</div>
		{/each}
		{#if $isDesktop && page.route.id == '/'}
			<ToggleSwitch size={'sm'} icon={!checked ? 'web_traffic' : 'tile_small'} bind:checked />
		{/if}
	</div>

	<div
		id="primary-nav"
		class={[
			'items-between absolute top-6 left-6 min-h-1/3 w-1/3 flex-col gap-3 bg-white p-6 transition-all duration-200 ease-linear',
			'lg:static lg:flex lg:h-full lg:w-1/12 lg:translate-y-0 lg:justify-between lg:p-0 lg:opacity-100',
			$isMenuOpen ? 'z-50 flex translate-y-0 opacity-100' : 'z-0 -translate-y-6 opacity-0'
		]}
		class:dashed-border={$isMenuOpen}
	>
		<Navbar {links} textClass={'text-uppercase text-base'} />
		{#if projectLinks}
			<Navbar links={projectLinks} textClass={'text-xs'} />
		{/if}
		<Navbar links={socialLinks} textClass={'text-xs'} />
	</div>

	<div
		class="relative h-full w-full overflow-y-auto scroll-smooth bg-white p-6"
		style="background-image:var(--dashed-border)"
		onscroll={onScroll}
		bind:clientWidth={containerWidth}
		bind:clientHeight={containerHeight}
	>
		{@render children?.()}
	</div>

	<div
		aria-hidden="true"
		class="pointer-events-none absolute top-6 right-6 z-10"
		style="background-image: var(--dashed-border);"
		style:width="{containerWidth}px"
		style:height="{containerHeight}px"
	></div>
	<div
		class="absolute right-6 bottom-6 z-10 mr-[0.5px] mb-[0.75px] ml-[0.5px] h-1/20 bg-gradient-to-t from-white to-transparent"
		style:width="{containerWidth - 1}px"
	></div>
	<div
		class="absolute top-6 right-6 z-10 mt-[0.5px] mr-[0.5px] ml-[0.5px] h-1/50 bg-gradient-to-b from-white to-transparent"
		style:width="{containerWidth - 1}px"
	></div>

	<div
		class={[
			'pointer-events-none absolute z-20 flex flex-col rounded-full px-2 py-1',
			$awards.length !== 0 && page.route.id == '/' && $isGridLayout ? 'opacity-100' : 'opacity-0'
		]}
		style:background={'rgba(255, 255, 255, 0.85)'}
		style:left={`${m.x}px`}
		style:top={`${m.y}px`}
		style:transform={`translate(-50%, 50%)`}
		style:width={'max-content'}
		style:transition={'opacity 0.3s linear'}
	>
		{#each $awards as a}
			<div class="w-max-content text-center text-xs">{a.split('(')[0].trim()}</div>
		{/each}
	</div>
</div>

<style>
	.dashed-border {
		background-image: var(--dashed-border);
	}
</style>
