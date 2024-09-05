<script lang="ts">
	import Button from "$lib/components/Button.svelte"
	import type { ComponentType } from "svelte";

	export let component: ComponentType;
	export let value: {};
	export let title: string = "";
</script>

<div>
	<h2>{title}</h2>
	<svelte:component this={component} bind:value></svelte:component>
	<Button>Save</Button>
	<Button>Cancel</Button>
</div>
