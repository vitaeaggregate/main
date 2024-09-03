<script lang='ts'>
	import { createEventDispatcher } from "svelte";
    import InputText from "$lib/components/InputText.svelte";
    import TextArea from "$lib/components/TextArea.svelte";

    let headerId: number;
    let inputName: string;
    let inputDescription: string;

    $: interest = {
        header: headerId,
        name: inputName,
        description: inputDescription,
    }

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", interest);
    }

</script>

<div class="flex flex-col">
    <h2>Interest</h2>
    <InputText label="Name" bind:value={inputName}/>
    <TextArea label="Description" bind:value={inputDescription}/>
</div>