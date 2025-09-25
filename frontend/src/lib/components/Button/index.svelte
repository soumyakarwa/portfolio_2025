<script lang="ts">
	interface Props {
		label: string;
		href?: string;
	}

	let { label, href = '' }: Props = $props();

	let active = $state(false);

	const handleClick = (event: MouseEvent) => {
		if (active) {
			event.preventDefault();
		}
	};
</script>

<a
	class={[
		active ? 'active' : '',
		'inline-block max-w-max cursor-pointer bg-white px-1 text-sm uppercase no-underline'
	]}
	{href}
	onclick={handleClick}
	target={'_blank'}
	rel={'noopener noreferrer'}
>
	{label}
</a>

<style>
	a {
		background-image: var(--dashed-border);
		transition:
			background-color 0.3s linear,
			color 0.3s linear;
	}

	a:hover {
		background-image: var(--dashed-border-white);
		background-color: black;
		color: white;
	}

	a.active {
		background-color: white;
		color: black;
	}

	a.active:hover {
		background-image: none;
		cursor: default;
	}
</style>
