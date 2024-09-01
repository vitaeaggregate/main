<script>
	import TextArea from "./TextArea.svelte";
	import InputText from "./InputText.svelte";
	import InputDate from "./InputDate.svelte";
</script>

<div class="flex flex-col">
    <h2>Professional Experience</h2>
        <InputText label="Job Title" placeholder="Put your job title here"></InputText>
        <InputText label="Employer" placeholder="Put the employer name here"></InputText>
        <InputText label="City" placeholder="Put the city name here"></InputText>
        <InputText label="Country" placeholder="Put the name of the country here"></InputText>
        <InputDate label="Start Date"></InputDate>
        <InputDate label="End Date"></InputDate>
        <TextArea label="Description" placeholder="Put the description here"></TextArea>
</div>