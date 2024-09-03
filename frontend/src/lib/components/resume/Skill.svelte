<script lang='ts'>
	import { createEventDispatcher } from "svelte";
    import InputText from "$lib/components/InputText.svelte";
    import TextArea from "$lib/components/TextArea.svelte";

    let resumeID: number = 0;
    let inputName: string = '';
    let inputDescription: string = '';
    let inputSkillLevel: string = '';

    $: skill = {
        resume: resumeID,
        name: inputName,
        description: inputDescription,
        skill_level: inputSkillLevel,
    }

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", skill)
    }

</script>



<div class="flex flex-col">
    <h2>Skills</h2>
    <InputText label="Name" bind:value={inputName}/>
    <TextArea label="Description" bind:value={inputDescription}/>
    <InputText label="Skill Level" bind:value={inputSkillLevel}/>
</div>