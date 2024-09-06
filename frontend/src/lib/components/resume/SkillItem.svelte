<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
	import type Skill from "$lib/interfaces/resume/Skill";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";

	export let value: Skill = {
		name: "",
		description: "",
		skill_level: ""
	};
	export let readOnly: boolean = false;

	onMount(() => {
		if (value.id) return;
		value.id = getRandomId();
	});
</script>

{#if readOnly}
	<div>
		<p><strong>Name:</strong> {value.name}</p>
		<p><strong>Description:</strong> {value.description}</p>
		<p><strong>Skill Level:</strong> {value.skill_level}</p>
	</div>
{:else}
	<div>
		<InputText label="Name" bind:value={value.name} />
		<TextArea label="Description" bind:value={value.description} />
		<InputText label="Skill Level" bind:value={value.skill_level} />
	</div>
{/if}
