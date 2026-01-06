import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const scrollY: Writable<number> = writable(0);
export const activeId: Writable<string> = writable('');
export const isMenuOpen: Writable<boolean> = writable(false);
export const isDesktop: Writable<boolean> = writable(false);
export const isGridLayout: Writable<boolean> = writable(false);
export const awards: Writable<string[]> = writable([]);
