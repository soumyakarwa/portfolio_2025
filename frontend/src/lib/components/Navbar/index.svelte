<script lang="ts">
	import { page } from '$app/state';
	import { activeId, isMenuOpen } from '$lib/components/Util/index';

	interface Props {
		links: {
			label: string;
			href: string;
		}[];
		textClass?: string;
		newTab?: boolean;
	}

	const { links, textClass, newTab = false }: Props = $props();
</script>

<div class="flex flex-col items-start justify-center lg:items-end">
	{#each links as link}
		<a
			class={[
				'p-[0.1rem] text-left uppercase lg:text-right',
				textClass,
				page.route.id === link.href || `#${$activeId}` == link.href ? 'active' : ''
			]}
			href={link.href}
			target={newTab ? '_blank' : undefined}
			rel={newTab ? 'noopener noreferrer' : undefined}
			onclick={() => ($isMenuOpen ? isMenuOpen.set(false) : null)}>{link.label}</a
		>
	{/each}
</div>

<style>
	a {
		background-image: none;
		transition: font-weight 0.3s linear;
	}

	a:hover {
		background-image: var(--dashed-border);
	}

	a.active {
		font-weight: 800;
	}

	a.active:hover {
		background-image: none;
		cursor: default;
	}
</style>
