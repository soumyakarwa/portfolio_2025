<script lang="ts">
	interface Props {
		label: string;
	}

	const labelLegend: Record<string, { bg: string; color: string }> = {
		Reuters: {
			bg: '#FFBC42',
			color: '#000'
		},
		Personal: {
			bg: '#D81159',
			color: '#fff'
		},
		Parsons: {
			bg: '#8F2D56',
			color: '#fff'
		},
		Freelance: {
			bg: '#218380',
			color: '#fff'
		},
		Dataface: {
			bg: '#73D2DE',
			color: '#000'
		}
	};

	let { label }: Props = $props();
</script>

<div
	class="font-regular max-h-max max-w-max rounded-full px-1 py-0.5 text-right text-xs uppercase"
	style:background-color={labelLegend[label].bg}
	style:color={labelLegend[label].color}
>
	{label}
</div>
