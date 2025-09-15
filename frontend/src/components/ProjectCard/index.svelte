<script lang="ts">
	interface Props {
		id: string;
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
	}

	let { id, wip, title, overview, tags, role, tech, content }: Props = $props();

	const randomPos = {
		top: `${Math.random() * 100}%`,
		left: `${Math.random() * 100}%`
	};
</script>

<div
	id={`project-${id}`}
	class={[
		'absolute flex h-1/2 w-1/3 flex-col gap-4 p-3 opacity-100 transition-opacity duration-100 ease-linear hover:cursor-pointer hover:opacity-100',
		`left-[${randomPos.left}] top-[${randomPos.top}]`
	]}
	style="background-image:var(--dashed-border)"
>
	<div class="h-4/10 w-full bg-black"></div>
	<div class="flex flex-col">
		<div class="text-base uppercase">{title}</div>
		<div class="text-xs">{overview}</div>
	</div>
</div>
