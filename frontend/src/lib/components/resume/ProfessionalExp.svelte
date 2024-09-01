<script>
	import TextArea from "./TextArea.svelte";
	import InputText from "./InputText.svelte";
	import InputDate from "./InputDate.svelte";
</script>

<div class="flex flex-col">
    <h2>Professional Experience</h2>
        <InputText label="Job Title"></InputText>
        <InputText label="Employer"></InputText>
        <InputText label="City"></InputText>
        <InputText label="Country"></InputText>
        <InputDate label="Start Date"></InputDate>
        <InputDate label="End Date"></InputDate>
        <TextArea label="Description"></TextArea>
</div>