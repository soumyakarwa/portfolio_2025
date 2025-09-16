<script lang="ts">
	interface Props {
		id: string;
		startingPos: number[];
		wip?: boolean;
		title: string;
		overview: string;
		tags?: string[];
		role?: string;
		tech?: string;
		content?: {
			title: string;
			description: string;
			images: string[];
		}[];
		isActive: boolean;
	}

	let { id, startingPos, wip, title, overview, tags, role, tech, content, isActive }: Props =
		$props();

	let imageWidth = $state(0);
	let imageHeight = $derived((imageWidth * 9) / 16);
</script>

<div
	class="absolute top-0 left-0 z-0 -translate-3/4 border-[0.5px] border-solid border-black bg-white"
	style:width="{imageWidth * 0.75}px"
	style:height="{imageHeight * 0.75}px"
></div>
<div
	id={`project-${id}`}
	class="absolute z-10 flex h-full w-full flex-col justify-around p-3"
	style:background-image="var(--dashed-border)"
>
	<div class="w-full bg-black" bind:clientWidth={imageWidth} style:height="{imageHeight}px"></div>
	<div class="flex flex-col">
		<div class="text-base uppercase">{title}</div>
		<div class="text-xs">{overview}</div>
	</div>
</div>
