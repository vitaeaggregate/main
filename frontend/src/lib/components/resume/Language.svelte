<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	export let value = {};

	let inputLanguage: string = "";
	let inputDescription: string = "";
	let inputSkillLevel: string = "";

	$: value = {
		language: inputLanguage,
		description: inputDescription,
		skill_level: inputSkillLevel
	};
</script>

<div class="flex flex-col">
	<h2>Language</h2>
	<InputText label="Language" bind:value={inputLanguage} />
	<TextArea label="Description" bind:value={inputDescription} />
	<InputText label="Skill Level" bind:value={inputSkillLevel} />
</div>
