<script lang='ts'>
    import TextArea from "$lib/components/TextArea.svelte";
    import InputText from "$lib/components/InputText.svelte";
    import InputDate from "$lib/components/InputDate.svelte";
    import type Publication from "$lib/interfaces/resume/Publication";
    import { getRandomId } from "$lib/utils";
    import { onMount } from "svelte";

    export let value: Publication = {
        title: "",
        publisher: "",
        date: undefined,
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
        <p><strong>Title:</strong> {value.title ? value.title : ""}</p>
        <p><strong>Publisher:</strong> {value.publisher ? value.publisher : ""}</p>
        <p><strong>Date:</strong> {value.date ? value.date : ""}</p>
        <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
    </div>
{:else}
    <div>
        <p class='req'>*</p>
        <InputText label="Title" bind:value={value.title} />
        <InputText label="Publisher" bind:value={value.publisher} />
        <InputDate label="Date" bind:value={value.date} />
        <TextArea label="Description" bind:value={value.description} />
    </div>
{/if}
