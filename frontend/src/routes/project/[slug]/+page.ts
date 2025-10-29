import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import projects from '$lib/assets/content/projects.json';

export const load: PageLoad = ({ params }) => {
	return projects.find((entry) => entry.id == params.slug);

	error(404, 'Not found');
};
