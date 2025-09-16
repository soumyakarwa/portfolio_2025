<script lang="ts">
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<div class="text-base font-bold uppercase">{data.title}</div>
