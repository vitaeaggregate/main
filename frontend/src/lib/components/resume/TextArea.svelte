<script lang="ts">
	export let label: string = "Text area";
	export let placeholder: string = label;
</script>

<label class="flex flex-col">
	{label}:
    <textarea placeholder={placeholder} class="border-2"></textarea>
</label>
