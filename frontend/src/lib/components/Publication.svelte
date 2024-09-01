<script lang='ts'>
    // import {onMount} from "svelte"
    import TextArea from "./resume/TextArea.svelte";
    import InputText from "./resume/InputText.svelte";
    import InputDate from "./resume/InputDate.svelte";
    // import Publication from "$lib/interfaces/publication";
    // onMount(async () => {
    //     const data = await fetch();
    // })
</script>

<div class="flex flex-col">
    <h2>Publications</h2>
    <InputText label="Title"/>
    <InputText label="Publisher"/>
    <InputDate label="Date"/>
    <TextArea label="Description"/>
</div>