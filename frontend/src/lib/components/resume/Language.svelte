<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
	import type Language from "$lib/interfaces/resume/Language";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";

	export let value: Language = {
		language: "",
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
		<p><strong>Language:</strong> {value.language ? value.language : ""}</p>
		<p><strong>Description:</strong> {value.description ? value.description : ""}</p>
		<p><strong>Skill Level:</strong> {value.skill_level ? value.skill_level : ""}</p>
	</div>
{:else}
	<div>
		<p class='req'>*</p>
		<InputText label="Language" bind:value={value.language} />
		<p class='req'>*</p>
		<TextArea label="Description" bind:value={value.description} />
		<p class='req'>*</p>
		<InputText label="Skill Level" bind:value={value.skill_level} />
	</div>
{/if}
