<script lang="ts">
	import { page } from '$app/state';

	interface Props {
		links: {
			label: string;
			href: string;
		}[];
		textClass?: string;
	}

	const { links, textClass }: Props = $props();
</script>

<div class="flex flex-col items-end justify-center">
	{#each links as link}
		<a
			class={['p-[0.1rem] uppercase', textClass, page.url.pathname === link.href ? 'active' : '']}
			href={link.href}>{link.label}</a
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
		font-weight: 700;
	}

	a.active:hover {
		background-image: none;
		cursor: default;
	}
</style>
