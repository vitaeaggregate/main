<script lang='ts'>
	import { createEventDispatcher } from "svelte";
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
    let resumeID: number = 0;
    let inputLanguage: string = '';
    let inputDescription: string = '';
    let inputSkillLevel: string = '';

    $:language = {
        resume: resumeID,
        language: inputLanguage,
        description: inputDescription,
        skill_level: inputSkillLevel,
    }

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", language)
    }

</script>
<div class="flex flex-col">
    <h2>Language</h2>
    <InputText label="Language" bind:value={inputLanguage}/>
    <TextArea label="Description" bind:value={inputDescription}/>
    <InputText label="Skill Level" bind:value={inputSkillLevel}/>
</div>