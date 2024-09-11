<script lang="ts">
	export let label: string = "Text area";
	export let placeholder: string = label;
	export let value: string = "";
	export let required:boolean = false; 
</script>

<label class="flex flex-col">
	{required ? "*": ""}
	{label}: 
	<textarea {placeholder} bind:value class="border-2 p-1 h-3/6"></textarea>
  </label>
