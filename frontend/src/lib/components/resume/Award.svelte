<script>
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
</script>

<div class="flex flex-col">
	<h2>Award</h2>
	<InputText label="Title"></InputText>
	<InputText label="Issuer"></InputText>
	<InputDate label="Date"></InputDate>
	<TextArea label="Description"></TextArea>
</div>
