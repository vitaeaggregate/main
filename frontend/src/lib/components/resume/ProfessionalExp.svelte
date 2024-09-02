<script>
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
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
