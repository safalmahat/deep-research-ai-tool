from agents import Runner, function_tool, trace, gen_trace_id
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData
import asyncio


""" class ResearchManager:

    async def run(self,query:str):
     Run the deep research process, yielding the status updates and the final report
        trace_id=gen_trace_id()
        with trace("Deep search research trace",trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research...")
            search_plan= await self.plan_searches(query)
            yield "Searches planned, starting to search..."     
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."
            report = await self.write_report(query, search_results)
            yield "Report written, sending email..."
            yield report.markdown_report 
            
            """


@function_tool
async def plan_searches(query:str) -> WebSearchPlan:
    """ Plan the search to perform query"""
    print("Planning searches...")
    result= await Runner.run(planner_agent, f"Query: {query}")
    print(f"will perform {len(result.final_output.searches)} searches")
    return result.final_output_as(WebSearchPlan)
    
@function_tool
async def perform_searches(search_plan:WebSearchPlan) -> WebSearchItem:
    """ Peform the searches to perform for the query"""
    print("Searching.....")
    num_completed=0
    tasks=[asyncio.create_task(search(item)) for item in search_plan.searches]
    results=[]
    for task in asyncio.as_completed(tasks):
        result= await task
        if result is not None:
            results.append(result)
        num_completed+=1
        print(f"Searching... {num_completed}/{len(tasks)} completed")
    print("Finished searching")
    return results


async def search(search_item:WebSearchItem)->str | None:
    """ Perform a search for the query """
    input=f" Search term = {search_item.query}\n Reason for searching: {search_item.reason}"
    try: 
        result=await Runner.run(search_agent,input)
        return str(result.final_output)
    except Exception:
        return None
        
@function_tool
async def write_report(query:str,search_results:list[str]) -> ReportData:
    """ Write the report for the query """
    print("Thinking about report...") 
    input=f"original query: {query}\n initial research done by a research assistant: {search_results}"
    result= await Runner.run(writer_agent,input)
    print("Finished writing report")
    return result.final_output_as(ReportData)      

