# shelly.py (Updated for Local LLM with Ollama)

import typer
import ollama
import subprocess
import pyperclip
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

# Initialize Rich Console
console = Console()
app = typer.Typer()

# --- Configuration ---
# The model we downloaded with Ollama
LOCAL_MODEL = "codellama:7b-instruct"

@app.command()
def generate(
    prompt: str = typer.Argument(..., help="Describe the command or script you need."),
    execute: bool = typer.Option(False, "--execute", "-e", help="Execute the generated command immediately."),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy the generated command to the clipboard.")
):
    """
    Generates shell commands or scripts using a local LLM.
    """
    console.print(f"[bold blue]🤖 Generating command for: '{prompt}' with local model '{LOCAL_MODEL}'...[/bold blue]")

    # The system prompt tells the AI how to behave.
    system_prompt = (
        "You are an expert shell command and script generator. "
        "Based on the user's request, provide ONLY the shell command or script as a direct response. "
        "Do not add any explanations, introductory text, or markdown code fences like ```bash. "
        "Just provide the raw command."
    )
    
    try:
        # Send the request to the local Ollama server
        response = ollama.chat(
            model=LOCAL_MODEL,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt},
            ],
        )
        
        # The generated command is in the 'content' of the response message
        generated_command = response['message']['content'].strip()

        if not generated_command:
            console.print("[bold red]❌ The model did not return a command. Try rephrasing.[/bold red]")
            raise typer.Exit()

        console.print("\n[bold green]✨ Generated Command:[/bold green]")
        syntax = Syntax(generated_command, "bash", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, border_style="green", title="Suggested Command"))

        if copy:
            pyperclip.copy(generated_command)
            console.print("\n[bold yellow]📋 Command copied to clipboard![/bold yellow]")

        if execute:
            console.print("\n")
            # SAFETY CHECK
            if typer.confirm(f"Are you sure you want to execute this command?"):
                console.print(f"[bold yellow]🚀 Executing...[/bold yellow]\n")
                try:
                    process = subprocess.run(
                        generated_command, shell=True, check=True, text=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                    console.print("[bold green]--- Output ---[/bold green]")
                    if process.stdout:
                        console.print(process.stdout)
                    if process.stderr:
                        console.print(f"[bold red]--- Errors ---[/bold red]\n{process.stderr}")
                    console.print("[bold green]✅ Execution finished successfully.[/bold green]")
                except subprocess.CalledProcessError as e:
                    console.print(f"[bold red]❌ Command failed with exit code {e.returncode}[/bold red]")
                    if e.stderr:
                        console.print(f"[bold red]--- Errors ---[/bold red]\n{e.stderr}")
            else:
                console.print("\n[bold red]Execution cancelled.[/bold red]")

    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")
        console.print("[bold yellow]Is the Ollama application running? You can start it by typing 'ollama serve' in your terminal.[/bold yellow]")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
