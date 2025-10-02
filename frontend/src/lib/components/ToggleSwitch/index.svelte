<script lang="ts">
	import { fade } from 'svelte/transition';

	type ToggleSize = 'sm' | 'md';

	interface Props {
		label?: string;
		icon?: string;
		srLabel?: string;
		disabled?: boolean;
		size?: ToggleSize;
		checked?: boolean;
	}

	const metricsBySize: Record<
		ToggleSize,
		{ trackWidth: number; trackHeight: number; knobSize: number; offset: number; iconClass: string }
	> = {
		sm: { trackWidth: 42, trackHeight: 22, knobSize: 18, offset: 2, iconClass: '!text-[0.9rem]' },
		md: { trackWidth: 52, trackHeight: 26, knobSize: 20, offset: 3, iconClass: '!text-[1rem]' }
	};

	let {
		label = '',
		icon,
		srLabel,
		disabled = false,
		size = 'md',
		checked = $bindable()
	}: Props = $props();

	let metrics = $derived(metricsBySize[size] ?? metricsBySize.md);
	let knobTravel = $derived(metrics.trackWidth - metrics.knobSize - metrics.offset * 2);
	let accessibleLabel = $derived(srLabel ?? label);

	const onChange = (event: Event) => {
		const input = event.currentTarget as HTMLInputElement;
		checked = input.checked;
	};
</script>

<label
	transition:fade
	class={[
		'group inline-flex items-center gap-3 text-xs font-semibold tracking-[0.08em] uppercase select-none',
		disabled ? 'cursor-not-allowed opacity-60' : 'cursor-pointer'
	]}
	aria-disabled={disabled}
>
	<input
		type="checkbox"
		class="sr-only"
		role="switch"
		aria-checked={checked}
		aria-label={accessibleLabel || undefined}
		{disabled}
		bind:checked
		onchange={onChange}
	/>

	{#if label}
		<span>{label}</span>
	{/if}
	<span
		class={[
			'relative inline-flex shrink-0 items-center overflow-hidden rounded-full border transition-colors duration-200 ease-out',
			checked ? 'border-black bg-black' : 'border-black bg-white',
			disabled ? 'opacity-70' : ''
		]}
		style:width={`${metrics.trackWidth}px`}
		style:height={`${metrics.trackHeight}px`}
	>
		<span
			class={[
				'absolute flex items-center justify-center rounded-full border transition-all duration-200 ease-out',
				checked ? 'border-black bg-white text-black' : 'border-white bg-black text-white'
			]}
			aria-hidden="true"
			style:top="50%"
			style:left={`${metrics.offset}px`}
			style:width={`${metrics.knobSize}px`}
			style:height={`${metrics.knobSize}px`}
			style:transform={`translateY(-50%) translateX(${checked ? knobTravel : 0}px)`}
		>
			{#if icon}
				<span class={['material-symbols-outlined leading-none', metrics.iconClass]}>{icon}</span>
			{/if}
		</span>
	</span>
</label>
