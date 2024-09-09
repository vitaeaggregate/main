<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
	import type Interest from "$lib/interfaces/resume/Interest";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";

	export let value: Interest = {
		name: "",
		description: ""
	};
	export let readOnly: boolean = false;

	onMount(() => {
		if (value.id) return;
		value.id = getRandomId();
	});
</script>

{#if readOnly}
	<div>
		<p><strong>Name:</strong> {value.name ? value.name : ""}</p>
		<p><strong>Description:</strong> {value.description ? value.description : ""}</p>
	</div>
{:else}
	<div>
		<InputText label="Name" bind:value={value.name} />
		<TextArea label="Description" bind:value={value.description} />
	</div>
{/if}
