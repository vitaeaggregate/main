<script>
	import InputDate from "./InputDate.svelte";
	import InputText from "./InputText.svelte";
	import TextArea from "./TextArea.svelte";
</script>

<div class="flex flex-col">
	<h2>Award</h2>
	<InputText label="Title"></InputText>
	<InputText label="Issuer"></InputText>
	<InputDate label="Date"></InputDate>
	<TextArea label="Description"></TextArea>
</div>
