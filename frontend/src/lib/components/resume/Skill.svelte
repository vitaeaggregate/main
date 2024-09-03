<script lang='ts'>
	import { createEventDispatcher } from "svelte";
    import InputText from "$lib/components/InputText.svelte";
    import TextArea from "$lib/components/TextArea.svelte";

    let headerId: number;
    let inputName: string;
    let inputDescription: string;
    let inputSkillLevel: string;

    $: skill = {
        header: headerId,
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