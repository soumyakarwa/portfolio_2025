<script lang="ts">
	interface Props {
		label: string;
	}

	let { label } = $props();
</script>

<div
	class="font-regular max-h-max max-w-max rounded-full bg-black px-1 py-0.5 text-right text-xs text-white uppercase"
>
	{label}
</div>
