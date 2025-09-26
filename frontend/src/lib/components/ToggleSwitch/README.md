# ToggleSwitch

Reusable toggle styled to match the portfolio shell. Supports optional Material Symbol icons, label text, and two-way binding on `checked`.

## Basic example

```svelte
<script lang="ts">
	import ToggleSwitch from '$lib/components/ToggleSwitch/index.svelte';

	let darkMode = false;
</script>

<ToggleSwitch label="Dark Mode" icon="dark_mode" bind:checked={darkMode} />
```

## Smaller toggle

```svelte
<ToggleSwitch label="Audio" icon="volume_up" size="sm" />
```

### Accessibility

- When the visual label is omitted, provide `srLabel` to keep an accessible name.
- The component dispatches `change` and `toggle` events with `{ checked, event }` details.
