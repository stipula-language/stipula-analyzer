// Generated from /home/cobalt/gitrepo/stipula-analyzer/Stipula.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link StipulaParser}.
 */
public interface StipulaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link StipulaParser#stipula}.
	 * @param ctx the parse tree
	 */
	void enterStipula(StipulaParser.StipulaContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#stipula}.
	 * @param ctx the parse tree
	 */
	void exitStipula(StipulaParser.StipulaContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#assetDecl}.
	 * @param ctx the parse tree
	 */
	void enterAssetDecl(StipulaParser.AssetDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#assetDecl}.
	 * @param ctx the parse tree
	 */
	void exitAssetDecl(StipulaParser.AssetDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#fieldDecl}.
	 * @param ctx the parse tree
	 */
	void enterFieldDecl(StipulaParser.FieldDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#fieldDecl}.
	 * @param ctx the parse tree
	 */
	void exitFieldDecl(StipulaParser.FieldDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#initStateDecl}.
	 * @param ctx the parse tree
	 */
	void enterInitStateDecl(StipulaParser.InitStateDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#initStateDecl}.
	 * @param ctx the parse tree
	 */
	void exitInitStateDecl(StipulaParser.InitStateDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#agreement}.
	 * @param ctx the parse tree
	 */
	void enterAgreement(StipulaParser.AgreementContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#agreement}.
	 * @param ctx the parse tree
	 */
	void exitAgreement(StipulaParser.AgreementContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#agree}.
	 * @param ctx the parse tree
	 */
	void enterAgree(StipulaParser.AgreeContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#agree}.
	 * @param ctx the parse tree
	 */
	void exitAgree(StipulaParser.AgreeContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(StipulaParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(StipulaParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void enterFunctionBody(StipulaParser.FunctionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void exitFunctionBody(StipulaParser.FunctionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(StipulaParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(StipulaParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#ifThenElse}.
	 * @param ctx the parse tree
	 */
	void enterIfThenElse(StipulaParser.IfThenElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#ifThenElse}.
	 * @param ctx the parse tree
	 */
	void exitIfThenElse(StipulaParser.IfThenElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#assetOperation}.
	 * @param ctx the parse tree
	 */
	void enterAssetOperation(StipulaParser.AssetOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#assetOperation}.
	 * @param ctx the parse tree
	 */
	void exitAssetOperation(StipulaParser.AssetOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#fieldOperation}.
	 * @param ctx the parse tree
	 */
	void enterFieldOperation(StipulaParser.FieldOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#fieldOperation}.
	 * @param ctx the parse tree
	 */
	void exitFieldOperation(StipulaParser.FieldOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#eventDecl}.
	 * @param ctx the parse tree
	 */
	void enterEventDecl(StipulaParser.EventDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#eventDecl}.
	 * @param ctx the parse tree
	 */
	void exitEventDecl(StipulaParser.EventDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#timeExpression}.
	 * @param ctx the parse tree
	 */
	void enterTimeExpression(StipulaParser.TimeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#timeExpression}.
	 * @param ctx the parse tree
	 */
	void exitTimeExpression(StipulaParser.TimeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#timeExpression1}.
	 * @param ctx the parse tree
	 */
	void enterTimeExpression1(StipulaParser.TimeExpression1Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#timeExpression1}.
	 * @param ctx the parse tree
	 */
	void exitTimeExpression1(StipulaParser.TimeExpression1Context ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(StipulaParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(StipulaParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression1}.
	 * @param ctx the parse tree
	 */
	void enterExpression1(StipulaParser.Expression1Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression1}.
	 * @param ctx the parse tree
	 */
	void exitExpression1(StipulaParser.Expression1Context ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterExpression2(StipulaParser.Expression2Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitExpression2(StipulaParser.Expression2Context ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression3}.
	 * @param ctx the parse tree
	 */
	void enterExpression3(StipulaParser.Expression3Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression3}.
	 * @param ctx the parse tree
	 */
	void exitExpression3(StipulaParser.Expression3Context ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression4}.
	 * @param ctx the parse tree
	 */
	void enterExpression4(StipulaParser.Expression4Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression4}.
	 * @param ctx the parse tree
	 */
	void exitExpression4(StipulaParser.Expression4Context ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression5}.
	 * @param ctx the parse tree
	 */
	void enterExpression5(StipulaParser.Expression5Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression5}.
	 * @param ctx the parse tree
	 */
	void exitExpression5(StipulaParser.Expression5Context ctx);
	/**
	 * Enter a parse tree produced by {@link StipulaParser#expression6}.
	 * @param ctx the parse tree
	 */
	void enterExpression6(StipulaParser.Expression6Context ctx);
	/**
	 * Exit a parse tree produced by {@link StipulaParser#expression6}.
	 * @param ctx the parse tree
	 */
	void exitExpression6(StipulaParser.Expression6Context ctx);
}