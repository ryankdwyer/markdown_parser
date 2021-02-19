"""Single entry point for all preprocessors."""

import src.impl.pre_processors.newline_processor as newline_processor
import src.impl.pre_processors.pre_processor_base as base

PreProcessorBase = base.PreProcessorBase
NewlineProcessor = newline_processor.NewlineProcessor
