from google.adk.agents import SequentialAgent

from ..preprocess import pre_processing
from ..embedding import embedding
from ..nlp import nlp
from ..orchestrator import orchestrator

contract_analysis = SequentialAgent(
    name="LeadQualificationPipeline",
    sub_agents=[pre_processing, embedding, nlp, orchestrator],
    description="A pipeline that validates, scores, and recommends actions for sales leads",
)